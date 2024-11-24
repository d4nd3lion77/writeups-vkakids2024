var encrypted = [89, 68, 78, 84, 95, 71, 28, 88, 112, 70, 91, 92, 112, 72, 31, 31, 75, 112, 91, 71, 27, 91, 112, 91, 71, 28, 93, 28, 112, 88, 27, 92, 112, 65, 31, 112, 66, 27, 67, 30, 76, 30, 64, 90, 92, 112, 76, 31, 75, 28, 82]
var key = 47;
function decrypt(encrypted, key) {
    var decrypted = "";
    for (var i = 0; i < encrypted.length; i++) {
        decrypted += String.fromCharCode(encrypted[i] ^ key);
    }
    return decrypted;
}
var correct = decrypt(encrypted, key);
var input = app.response("Enter flag:");
function checkFlag(input, flag) {
    if (input.length !== flag.length) {
        return false;
    }
    for (var i = 0; i < flag.length; i++) {
        if (input[i] !== flag[i]) {
            return false;
        }
    }
    return true;
}
if (checkFlag(input, correct)) {
    app.alert("Correct flag!");
} else {
    app.alert("Incorrect flag.");
}