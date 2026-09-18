import QtQuick 6.5
import QtQuick.Controls 6.5
import QtQuick.Layouts 6.5

ColumnLayout {
    id: root

    property string mode: "hsv"

    signal rangeChanged(string mode, var lower, var upper)

    HsvRangePicker {
        id: hsvPicker
        Layout.fillWidth: true
        visible: root.mode === "hsv"

        onHValueChanged: root.notify()
        onSValueChanged: root.notify()
        onVValueChanged: root.notify()
    }

    RgbRangePicker {
        id: rgbPicker
        Layout.fillWidth: true
        visible: root.mode === "rgb"

        onRValueChanged: root.notify()
        onGValueChanged: root.notify()
        onBValueChanged: root.notify()
    }

    Label {
        text: root.mode === "hsv"
              ? `LOWER [${hsvPicker.lower()}], UPPER [${hsvPicker.upper()}]`
              : `LOWER [${rgbPicker.lower()}], UPPER [${rgbPicker.upper()}]`
    }

    function setMode(mode) {
        root.mode = mode;
        root.notify();
    }

    function notify() {
        const picker = root.mode === "hsv" ? hsvPicker : rgbPicker;
        root.rangeChanged(root.mode, picker.lower(), picker.upper());
    }
}
