import QtQuick 2.5
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.2

Rectangle {
    visible: true
    width: 600
    height: 400
    color: "whitesmoke"

    GridLayout {
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.margins: 9

        columns: 4
        rows: 4
        rowSpacing: 10
        columnSpacing: 10

        // Input field of the first number



        Button {
            height: 40
            Layout.fillWidth: true
            text: qsTr("Do it")

            Layout.columnSpan: 2

            onClicked: {
                // Invoke the calculator slot to sum the numbers
                tool_changer.rotate_atc(1)
            }
        }
    }

    Image {
        id: atc_holder
        x: 143
        y: 43
        width: 314
        height: 314
        antialiasing: true
        z: 0
        rotation: 0
        transformOrigin: Item.Center
        source: "images/carousel_12.png"

        property int rotate_plus: 360/12
        property int rotate_minus: 360/12
        property int back: 3

        Rectangle {
            id: tool_1
            x: 271
            y: 136
            width: 42
            height: 42
            color: "#ffffff"
            radius: 21
            border.width: 2

            Text {
                id: tool_text_1
                x: 8
                y: 7
                text: qsTr("T1")
                font.bold: true
                verticalAlignment: Text.AlignVCenter
                horizontalAlignment: Text.AlignHCenter
                font.pixelSize: 22
            }
        }

        Rectangle {
            id: tool_2
            x: 253
            y: 68
            width: 42
            height: 42
            color: "#ffffff"
            radius: 21
            border.width: 2

            Text {
                id: tool_text_2
                x: 8
                y: 6
                text: qsTr("T2")
                font.bold: true
                verticalAlignment: Text.AlignVCenter
                horizontalAlignment: Text.AlignHCenter
                font.pixelSize: 22
            }
        }

        Rectangle {
            id: tool_3
            x: 204
            y: 19
            width: 42
            height: 42
            color: "#ffffff"
            radius: 21
            border.width: 2

            Text {
                id: tool_text_3
                x: 7
                y: 6
                text: qsTr("T3")
                font.bold: true
                verticalAlignment: Text.AlignVCenter
                horizontalAlignment: Text.AlignHCenter
                font.pixelSize: 22
            }
        }

        Rectangle {
            id: tool_4
            x: 136
            y: 1
            width: 42
            height: 42
            color: "#ffffff"
            radius: 21
            border.width: 2

            Text {
                id: tool_text_4
                x: 8
                y: 5
                text: qsTr("T4")
                font.bold: true
                verticalAlignment: Text.AlignVCenter
                horizontalAlignment: Text.AlignHCenter
                font.pixelSize: 22
            }
        }

        Rectangle {
            id: tool_5
            x: 68
            y: 19
            width: 42
            height: 42
            color: "#ffffff"
            radius: 21
            border.width: 2

            Text {
                id: tool_text_5
                x: 7
                y: 6
                text: qsTr("T5")
                font.bold: true
                verticalAlignment: Text.AlignVCenter
                horizontalAlignment: Text.AlignHCenter
                font.pixelSize: 22
            }
        }

        Rectangle {
            id: tool_6
            x: 19
            y: 69
            width: 42
            height: 42
            color: "#ffffff"
            radius: 21
            border.width: 2

            Text {
                id: tool_text_6
                x: 7
                y: 6
                text: qsTr("T6")
                font.bold: true
                verticalAlignment: Text.AlignVCenter
                horizontalAlignment: Text.AlignHCenter
                font.pixelSize: 22
            }
        }

        Rectangle {
            id: tool_7
            x: 1
            y: 136
            width: 42
            height: 42
            color: "#ffffff"
            radius: 21
            border.width: 2

            Text {
                id: tool_text_7
                x: 7
                y: 7
                text: qsTr("T7")
                font.bold: true
                verticalAlignment: Text.AlignVCenter
                horizontalAlignment: Text.AlignHCenter
                font.pixelSize: 22
            }
        }

        Rectangle {
            id: tool_8
            x: 19
            y: 204
            width: 42
            height: 42
            color: "#ffffff"
            radius: 21
            border.width: 2

            Text {
                id: tool_text_8
                x: 7
                y: 6
                text: qsTr("T8")
                font.bold: true
                verticalAlignment: Text.AlignVCenter
                horizontalAlignment: Text.AlignHCenter
                font.pixelSize: 22
            }
        }

        Rectangle {
            id: tool_9
            x: 68
            y: 253
            width: 42
            height: 42
            color: "#ffffff"
            radius: 21
            border.width: 2

            Text {
                id: tool_text_9
                x: 7
                y: 6
                text: qsTr("T9")
                font.bold: true
                verticalAlignment: Text.AlignVCenter
                horizontalAlignment: Text.AlignHCenter
                font.pixelSize: 22
            }
        }

        Rectangle {
            id: tool_10
            x: 136
            y: 271
            width: 42
            height: 42
            color: "#ffffff"
            radius: 21
            border.width: 2

            Text {
                id: tool_text_10
                x: 2
                y: 6
                text: qsTr("T10")
                font.bold: true
                verticalAlignment: Text.AlignVCenter
                horizontalAlignment: Text.AlignHCenter
                font.pixelSize: 22
            }
        }

        Rectangle {
            id: tool_11
            x: 204
            y: 253
            width: 42
            height: 42
            color: "#ffffff"
            radius: 21
            border.width: 2

            Text {
                id: tool_text_11
                x: 2
                y: 6
                text: qsTr("T11")
                font.bold: true
                verticalAlignment: Text.AlignVCenter
                horizontalAlignment: Text.AlignHCenter
                font.pixelSize: 22
            }
        }

        Rectangle {
            id: tool_12
            x: 253
            y: 203
            width: 42
            height: 42
            color: "#ffffff"
            radius: 21
            border.width: 2

            Text {
                id: tool_text_12
                x: 2
                y: 6
                text: qsTr("T12")
                font.bold: true
                verticalAlignment: Text.AlignVCenter
                horizontalAlignment: Text.AlignHCenter
                font.pixelSize: 22
            }
        }
    }

    // Here we take the result of sum or subtracting numbers
    Connections {
        target: tool_changer

        // Sum signal handler
        onChangeResult: {
            // sum was set through arguments=['test']
            atc_holder.rotation = change

            tool_1.rotation = -change
            tool_2.rotation = -change
            tool_3.rotation = -change
            tool_4.rotation = -change
            tool_5.rotation = -change
            tool_6.rotation = -change
            tool_7.rotation = -change
            tool_8.rotation = -change
            tool_9.rotation = -change
            tool_10.rotation = -change
            tool_11.rotation = -change
            tool_12.rotation = -change
        }
    }

}
