Java.perform(function() {
    function getPassword() {
        Java.choose('com.pwnsec.firestorm.MainActivity', {
            onMatch: function(instance) {
                console.log("MainActivity instance found: " + instance);
                try {
                    var pass = instance.Password();
                    console.log("FireBase Password: " + pass);
                } catch (e) {
                    console.log("Error occurred: " + e);
                }
            },
            onComplete: function() {
                console.log("Search completed. Exiting script.");

            }
        });
    }

    // Delay execution to ensure the app is fully started
    setTimeout(getPassword, 4000); // Adjust the delay as needed (4000 ms = 4 seconds)
});
