Java.perform(function(){
    const JavaString = Java.use("java.lang.String");
    Java.use("android.app.Activity").onUserInteraction.implementation = function() { 
        var AlertDialogBuilder = Java.use("android.app.AlertDialog$Builder"); 
        console.log('No Protection Againts Dyanmic Instrumentation'); 
        var test = JavaString.$new.overload("java.lang.String").call(JavaString,"Motion (Dynamic Instrumentation)"); 
        var alert = AlertDialogBuilder.$new(this);
        alert.setTitle(test);
        alert.setMessage(test);
        alert.create().show();
        return this.onUserInteraction();
    };
});