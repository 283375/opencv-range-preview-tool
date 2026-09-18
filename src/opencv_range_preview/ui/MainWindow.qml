import QtQuick 6.5
import QtQuick.Controls 6.5
import QtQuick.Dialogs 6.5
import QtQuick.Layouts 6.5

ApplicationWindow {
    id: window

    property color maskBgColor: "#ffffff"

    visible: true
    width: 960
    height: 600
    title: qsTr("opencv range preview")

    component ImagePane: ColumnLayout {
        id: pane

        property alias caption: captionLabel.text
        property alias baseUrl: image.sourcePrefix
        property int version

        Label {
            id: captionLabel
        }

        Rectangle {
            Layout.fillWidth: true
            Layout.fillHeight: true

            border.color: palette.mid
            color: palette.base

            Image {
                id: image

                property string sourcePrefix

                anchors.fill: parent
                anchors.margins: 4
                cache: false
                fillMode: Image.PreserveAspectFit
                source: pane.version > 0 ? sourcePrefix + "?v=" + pane.version : ""
            }

            Label {
                anchors.centerIn: parent
                visible: pane.version === 0
                text: qsTr("no image")
            }
        }
    }

    // Fusion colors checked indicators with the system accent color and
    // ignores palette overrides, so draw the indicator in monochrome here.
    component ClassicRadioButton: RadioButton {
        indicator: Rectangle {
            implicitWidth: 14
            implicitHeight: 14
            x: leftPadding
            y: topPadding + availableHeight / 2 - height / 2
            radius: width / 2
            color: "transparent"
            border.width: hovered ? 2 : 1
            border.color: checked || hovered ? palette.text : palette.mid

            Rectangle {
                anchors.centerIn: parent
                width: 6
                height: 6
                radius: width / 2
                color: palette.text
                visible: checked
            }
        }
    }

    header: ToolBar {
        RowLayout {
            anchors.fill: parent

            Button {
                text: qsTr("Load Image")
                onClicked: fileDialog.open()
            }

            ClassicRadioButton {
                checked: true
                text: qsTr("HSV")
                ButtonGroup.group: colorModeGroup
                onToggled: if (checked) rangeEditor.setMode("hsv")
            }

            ClassicRadioButton {
                text: qsTr("RGB")
                ButtonGroup.group: colorModeGroup
                onToggled: if (checked) rangeEditor.setMode("rgb")
            }

            ButtonGroup {
                id: colorModeGroup
            }

            Item {
                Layout.fillWidth: true
            }

            TabBar {
                id: maskTabBar

                objectName: "maskTabBar"

                TabButton {
                    width: implicitWidth
                    text: qsTr("Masked BW")
                }
                TabButton {
                    width: implicitWidth
                    text: qsTr("Masked Color")
                }

                onCurrentIndexChanged: backend.setColorMask(currentIndex === 1)
            }

            ToolButton {
                id: bgColorButton

                objectName: "bgColorButton"
                enabled: maskTabBar.currentIndex === 1
                opacity: enabled ? 1 : 0.3
                implicitWidth: 26
                implicitHeight: 24

                ToolTip.visible: hovered
                ToolTip.text: qsTr("Mask background color")

                onClicked: bgColorDialog.open()

                contentItem: Rectangle {
                    color: window.maskBgColor
                    border.color: palette.mid
                }
            }
        }
    }

    FileDialog {
        id: fileDialog

        nameFilters: [qsTr("Image (*.png *.jpg *.jpeg)"), qsTr("All files (*)")]
        onAccepted: backend.loadImage(selectedFile)
    }

    ColorDialog {
        id: bgColorDialog

        selectedColor: window.maskBgColor
        onAccepted: {
            window.maskBgColor = selectedColor;
            backend.setBackgroundColor(selectedColor);
        }
    }

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 8
        spacing: 8

        RangeEditor {
            id: rangeEditor

            Layout.fillWidth: true

            onRangeChanged: (mode, lower, upper) => backend.setRange(mode, lower, upper)
        }

        RowLayout {
            id: imagesRow

            Layout.fillWidth: true
            Layout.fillHeight: true

            ImagePane {
                Layout.fillWidth: true
                Layout.fillHeight: true
                // fillWidth alone is weighted by implicit width, which
                // differs with the caption; a zero preferred width makes
                // the row split the space exactly in half
                Layout.preferredWidth: 0

                caption: qsTr("ORIGINAL")
                baseUrl: "image://preview/orig"
                version: backend.origVersion
            }

            ImagePane {
                Layout.fillWidth: true
                Layout.fillHeight: true
                Layout.preferredWidth: 0

                caption: qsTr("OUTPUT")
                baseUrl: "image://preview/mask"
                version: backend.maskVersion
            }
        }
    }
}
