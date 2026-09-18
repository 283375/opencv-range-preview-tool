import QtQuick 6.5
import QtQuick.Layouts 6.5

ColumnLayout {
    id: root

    property alias rLower: rInput.firstValue
    property alias rUpper: rInput.secondValue
    property alias gLower: gInput.firstValue
    property alias gUpper: gInput.secondValue
    property alias bLower: bInput.firstValue
    property alias bUpper: bInput.secondValue

    signal rValueChanged(int lower, int upper)
    signal gValueChanged(int lower, int upper)
    signal bValueChanged(int lower, int upper)

    function lower() {
        return [rLower, gLower, bLower];
    }

    function upper() {
        return [rUpper, gUpper, bUpper];
    }

    RangeSliderWithSpinBoxes {
        id: rInput
        Layout.fillWidth: true
        from: 0
        to: 255
        stepSize: 1

        labelText: "R"

        onValueChanged: (l, h) => root.rValueChanged(l, h)
    }

    RangeSliderWithSpinBoxes {
        id: gInput
        Layout.fillWidth: true
        from: 0
        to: 255
        stepSize: 1

        labelText: "G"

        onValueChanged: (l, h) => root.gValueChanged(l, h)
    }

    RangeSliderWithSpinBoxes {
        id: bInput
        Layout.fillWidth: true
        from: 0
        to: 255
        stepSize: 1

        labelText: "B"

        onValueChanged: (l, h) => root.bValueChanged(l, h)
    }
}
