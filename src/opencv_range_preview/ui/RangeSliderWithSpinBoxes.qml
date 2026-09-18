import QtQuick 6.5
import QtQuick.Controls 6.5
import QtQuick.Layouts 6.5

RowLayout {
    id: root

    property alias labelText: label.text
    property alias from: slider.from
    property alias to: slider.to
    property alias firstValue: firstSpinBox.value
    property alias secondValue: secondSpinBox.value
    property alias stepSize: slider.stepSize

    signal valueChanged(int first, int second)

    spacing: 4

    onFirstValueChanged: {
        valueChanged(firstSpinBox.value, secondSpinBox.value);
    }
    onSecondValueChanged: {
        valueChanged(firstSpinBox.value, secondSpinBox.value);
    }

    Label {
        id: label

        Layout.minimumWidth: 20

        text: ""
    }

    RangeSlider {
        id: slider
        Layout.fillWidth: true
        snapMode: RangeSlider.SnapAlways

        first.onMoved: {
            firstSpinBox.value = first.value;
        }
        second.onMoved: {
            secondSpinBox.value = second.value;
        }
    }

    SpinBox {
        id: firstSpinBox
        from: slider.from
        to: slider.to
        stepSize: slider.stepSize
        // ValueModified skips programmatic updates, so syncing on it
        // avoids ping-ponging with the slider's onMoved handlers.
        onValueModified: {
            slider.first.value = value;
        }
    }

    SpinBox {
        id: secondSpinBox
        from: slider.from
        to: slider.to
        stepSize: slider.stepSize
        onValueModified: {
            slider.second.value = value;
        }
    }
}
