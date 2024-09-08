import QtQuick
import QtQuick.Controls


ApplicationWindow{
    width: 600
    height: 600
    title: "My Form"
    visible: true
    color: "black"

    Button{
        text: "Button"
        x: 100
        y: 100
    }

    Button{
        text: "Click Me"
        x: 200
        y: 100
    }

    Text{
        text: "I'm a label"
        color: "white"
    }

    TextField{
        placeholderText: "Name"
        y: 50
    }
}
