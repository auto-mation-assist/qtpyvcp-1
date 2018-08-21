import QtQuick 2.5
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.2

Item {
    visible: true
    width: 600
    height: 400

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
                main.rotate_forward(1)
            }
        }
        TextField {
            id: tool_num
            placeholderText: qsTr("Enter Tool")
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


        RotationAnimator {
            id: atc_anim
            target: atc_holder;
            duration: 3000
            running: false

            easing {
                type: Easing.OutElastic
                amplitude: 1
                period: 0.5
            }
        }

        Rectangle {
            id: tool_1
            x: 271
            y: 136
            width: 42
            height: 42
            color: "#ffffff"
            radius: 21
            border.width: 2

            RotationAnimator {
                id: tool_anim_1
                target: tool_1;
                duration: 3000
                running: false

                easing {
                    type: Easing.OutElastic
                    amplitude: 1
                    period: 0.5
                }
            }

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

            RotationAnimator {
                id: tool_anim_2
                target: tool_2;
                duration: 3000
                running: false

                easing {
                    type: Easing.OutElastic
                    amplitude: 1
                    period: 0.5
                }
            }

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

            RotationAnimator {
                id: tool_anim_3
                target: tool_3;
                duration: 3000
                running: false

                easing {
                    type: Easing.OutElastic
                    amplitude: 1
                    period: 0.5
                }
            }

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

            RotationAnimator {
                id: tool_anim_4
                target: tool_4;
                duration: 3000
                running: false

                easing {
                    type: Easing.OutElastic
                    amplitude: 1
                    period: 0.5
                }
            }

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

            RotationAnimator {
                id: tool_anim_5
                target: tool_5;
                duration: 3000
                running: false

                easing {
                    type: Easing.OutElastic
                    amplitude: 1
                    period: 0.5
                }
            }

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

            RotationAnimator {
                id: tool_anim_6
                target: tool_6;
                duration: 3000
                running: false

                easing {
                    type: Easing.OutElastic
                    amplitude: 1
                    period: 0.5
                }
            }

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

            RotationAnimator {
                id: tool_anim_7
                target: tool_7;
                duration: 3000
                running: false

                easing {
                    type: Easing.OutElastic
                    amplitude: 1
                    period: 0.5
                }
            }

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

            RotationAnimator {
                id: tool_anim_8
                target: tool_8;
                duration: 3000
                running: false

                easing {
                    type: Easing.OutElastic
                    amplitude: 1
                    period: 0.5
                }
            }

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

            RotationAnimator {
                id: tool_anim_9
                target: tool_9;
                duration: 3000
                running: false

                easing {
                    type: Easing.OutElastic
                    amplitude: 1
                    period: 0.5
                }
            }

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

            RotationAnimator {
                id: tool_anim_10
                target: tool_10;
                duration: 3000
                running: false

                easing {
                    type: Easing.OutElastic
                    amplitude: 1
                    period: 0.5
                }
            }

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

            RotationAnimator {
                id: tool_anim_11
                target: tool_11;
                duration: 3000
                running: false

                easing {
                    type: Easing.OutElastic
                    amplitude: 1
                    period: 0.5
                }
            }

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

            RotationAnimator {
                id: tool_anim_12
                target: tool_12;
                duration: 3000
                running: false

                easing {
                    type: Easing.OutElastic
                    amplitude: 1
                    period: 0.5
                }
            }

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

    Timer {
        id: halTimer
        interval: 100
        repeat: true
        running: true
        triggeredOnStart: true
        onTriggered: main.get_pins()
    }

    // Here we take the result of sum or subtracting numbers
    Connections {
        target: main
        // Sum signal handler
        onRotateFwdSig: {
            atc_anim.from = (360/12 * rotate_forward)
            atc_anim.to = (360/12 * rotate_forward + 360/12)
            atc_anim.restart()

            tool_anim_1.from = -(360/12 * rotate_forward)
            tool_anim_1.to = -(360/12 * rotate_forward + 360/12)
            tool_anim_1.restart()

            tool_anim_2.from = -(360/12 * rotate_forward)
            tool_anim_2.to = -(360/12 * rotate_forward + 360/12)
            tool_anim_2.restart()

            tool_anim_3.from = -(360/12 * rotate_forward)
            tool_anim_3.to = -(360/12 * rotate_forward + 360/12)
            tool_anim_3.restart()

            tool_anim_4.from = -(360/12 * rotate_forward)
            tool_anim_4.to = -(360/12 * rotate_forward + 360/12)
            tool_anim_4.restart()

            tool_anim_5.from = -(360/12 * rotate_forward)
            tool_anim_5.to = -(360/12 * rotate_forward + 360/12)
            tool_anim_5.restart()

            tool_anim_6.from = -(360/12 * rotate_forward)
            tool_anim_6.to = -(360/12 * rotate_forward + 360/12)
            tool_anim_6.restart()

            tool_anim_7.from = -(360/12 * rotate_forward)
            tool_anim_7.to = -(360/12 * rotate_forward + 360/12)
            tool_anim_7.restart()

            tool_anim_8.from = -(360/12 * rotate_forward)
            tool_anim_8.to = -(360/12 * rotate_forward + 360/12)
            tool_anim_8.restart()

            tool_anim_9.from = -(360/12 * rotate_forward)
            tool_anim_9.to = -(360/12 * rotate_forward + 360/12)
            tool_anim_9.restart()

            tool_anim_10.from = -(360/12 * rotate_forward)
            tool_anim_10.to = -(360/12 * rotate_forward + 360/12)
            tool_anim_10.restart()

            tool_anim_11.from = -(360/12 * rotate_forward)
            tool_anim_11.to = -(360/12 * rotate_forward + 360/12)
            tool_anim_11.restart()

            tool_anim_12.from = -(360/12 * rotate_forward)
            tool_anim_12.to = -(360/12 * rotate_forward + 360/12)
            tool_anim_12.restart()

        }
        // Sum signal handler
        onRotateRevSig: {
            atc_anim.from = (360/12 * rotate_reverse)
            atc_anim.to = (360/12 * rotate_reverse + 360/12)
            atc_anim.restart()

            tool_anim_1.from = -(360/12 * rotate_reverse)
            tool_anim_1.to = -(360/12 * rotate_reverse + 360/12)
            tool_anim_1.restart()

            tool_anim_2.from = -(360/12 * rotate_reverse)
            tool_anim_2.to = -(360/12 * rotate_reverse + 360/12)
            tool_anim_2.restart()

            tool_anim_3.from = -(360/12 * rotate_reverse)
            tool_anim_3.to = -(360/12 * rotate_reverse + 360/12)
            tool_anim_3.restart()

            tool_anim_4.from = -(360/12 * rotate_reverse)
            tool_anim_4.to = -(360/12 * rotate_reverse + 360/12)
            tool_anim_4.restart()

            tool_anim_5.from = -(360/12 * rotate_reverse)
            tool_anim_5.to = -(360/12 * rotate_reverse + 360/12)
            tool_anim_5.restart()

            tool_anim_6.from = -(360/12 * rotate_reverse)
            tool_anim_6.to = -(360/12 * rotate_reverse + 360/12)
            tool_anim_6.restart()

            tool_anim_7.from = -(360/12 * rotate_reverse)
            tool_anim_7.to = -(360/12 * rotate_reverse + 360/12)
            tool_anim_7.restart()

            tool_anim_8.from = -(360/12 * rotate_reverse)
            tool_anim_8.to = -(360/12 * rotate_reverse + 360/12)
            tool_anim_8.restart()

            tool_anim_9.from = -(360/12 * rotate_reverse)
            tool_anim_9.to = -(360/12 * rotate_reverse + 360/12)
            tool_anim_9.restart()

            tool_anim_10.from = -(360/12 * rotate_reverse)
            tool_anim_10.to = -(360/12 * rotate_reverse + 360/12)
            tool_anim_10.restart()

            tool_anim_11.from = -(360/12 * rotate_reverse)
            tool_anim_11.to = -(360/12 * rotate_reverse + 360/12)
            tool_anim_11.restart()

            tool_anim_12.from = -(360/12 * rotate_reverse)
            tool_anim_12.to = -(360/12 * rotate_reverse + 360/12)
            tool_anim_12.restart()

        }
    }

}
