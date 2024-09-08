import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material
import QtQuick.Layouts


ApplicationWindow{
    width: 500
    height: 300
    title: "My Form"
    visible: true
    Material.theme: Material.Dark
    Material.accent: Material.LightBlue

    ColumnLayout{
        TextField{
            placeholderText: "Name"
        }

        TextField{
            placeholderText: "Email"
        }

        TextField{
            placeholderText: "Address"
        }

        Button{
            text: "Save Data"
        }
    }
}
