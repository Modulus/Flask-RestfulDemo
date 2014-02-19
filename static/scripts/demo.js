/**
 * Created with IntelliJ IDEA.
 * User: john
 * Date: 22/10/13
 * Time: 14:33
 * To change this template use File | Settings | File Templates.
 */
$(function () {
    var indexViewModel = new IndexViewModel();
    indexViewModel.loadUsers();
    indexViewModel.loadMessages();

    ko.applyBindings(indexViewModel);
});

function IndexViewModel() {
    var self = this;
    this.users = ko.observableArray([]);
    this.messages = ko.observableArray([]);
    this.loadUsers = function () {
        $.getJSON("/users", function (allData) {
            self.users.removeAll();
            $.each(allData, function (index, item) {
                self.users.push(new User(item));

            });
        });
    }
    this.loadMessages = function(){
        $.getJSON("/messages", function(data){
            self.messages.removeAll();
            $.each(data, function(index, item){
               self.messages.push(new Message(item));
            });
        });
    }
}

function User(data) {
    this.firstName = data.firstName;
    this.lastName = data.lastName;
    this.userName = data.userName;
    this.hash = data.passHash;
    this.image = data.imagePath;
    this.birthDate = data.birthDate;
    this.joined = data.creationDate;
}

function Message(data){
    this.subject = data.subject;
    this.message = data.text;
    this.sender = new UserNested(data.sender);
    this.receiver = new UserNested(data.receiver);
}

function UserNested(data){
    var self = this;
    this.firstName = data.firstName;
    this.lastName = data.lastName;
    this.userName = data.userName;

    this.fullName = function(){
        return self.firstName  + " " + self.lastName;
    }
}


