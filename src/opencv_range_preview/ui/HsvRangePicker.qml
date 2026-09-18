import QtQuick 6.5
import QtQuick.Layouts 6.5

ColumnLayout {
    id: root

    property alias hLower: hInput.firstValue
    property alias hUpper: hInput.secondValue
    property alias sLower: sInput.firstValue
    property alias sUpper: sInput.secondValue
    property alias vLower: vInput.firstValue
    property alias vUpper: vInput.secondValue

    signal hValueChanged(int lower, int upper)
    signal sValueChanged(int lower, int upper)
    signal vValueChanged(int lower, int upper)

    function lower() {
        return [hLower, sLower, vLower];
    }

    function upper() {
        return [hUpper, sUpper, vUpper];
    }

    RangeSliderWithSpinBoxes {
        id: hInput
        Layout.fillWidth: true
        from: 0
        to: 179
        stepSize: 1

        labelText: "H"

        onValueChanged: (l, h) => root.hValueChanged(l, h)
    }

    RangeSliderWithSpinBoxes {
        id: sInput
        Layout.fillWidth: true
        from: 0
        to: 255
        stepSize: 1

        labelText: "S"

        onValueChanged: (l, h) => root.sValueChanged(l, h)
    }

    RangeSliderWithSpinBoxes {
        id: vInput
        Layout.fillWidth: true
        from: 0
        to: 255
        stepSize: 1

        labelText: "V"

        onValueChanged: (l, h) => root.vValueChanged(l, h)
    }
}
