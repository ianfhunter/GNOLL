var script = document.createElement('script')

script.setAttribute('src', 'gnoll.js');

script.onload = function(){
    var app = new Module({
        // print: function (e){
        //     console.log(e)
        // },
        onRuntimeInitialized: function(e){
            v = app.ccall("roll", "1d20");
            console.log(v)
        }
    })
}
document.body.appendChild(script)