pragma ComponentBehavior: Bound
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.VectorImage

import "../libs/formatters.mjs" as Formatters

RowLayout {
    id: root

    required property var playResult
    property alias pr: root.playResult

    spacing: 8

    SystemPalette {
        id: systemPalette
    }

    component PFLLabel: RowLayout {
        required property string label
        required property var value
        property color color: systemPalette.text

        spacing: 0.5

        Label {
            Layout.alignment: Qt.AlignBaseline

            text: parent.label
            font.pointSize: 8
            font.bold: true
            color: parent.color
        }

        Label {
            Layout.alignment: Qt.AlignBaseline
            text: parent.value ?? '-'
            color: parent.color
        }
    }

    function getGradeIcon(gradeLabel: string): string {
        const scheme = Application.styleHints.colorScheme == Qt.ColorScheme.Dark ? 'dark' : 'light';
        const filenameMap = {
            'EX+': 'ex-plus',
            'EX': 'ex',
            'AA': 'aa',
            'A': 'a',
            'B': 'b',
            'C': 'c',
            'D': 'd'
        };

        let filenameBase = filenameMap[gradeLabel];
        if (scheme === 'dark') {
            filenameBase += '-dark';
        }

        return `qrc:/images/grades/${filenameBase}.svg`;
    }

    TextMetrics {
        id: gradeTextMetrics
        text: 'EX+'

        font.pointSize: 18
        font.bold: true
    }

    VectorImage {
        id: gradeIcon
        Layout.preferredWidth: gradeTextMetrics.width
        Layout.preferredHeight: gradeTextMetrics.width

        fillMode: VectorImage.PreserveAspectFit
        preferredRendererType: VectorImage.CurveRenderer
        source: root.getGradeIcon(Formatters.scoreToGrade(root.pr.score))
    }

    ColumnLayout {
        Layout.fillWidth: true
        spacing: 1

        Label {
            Layout.fillWidth: true
            text: root.pr.score
            font.pointSize: 16
        }

        RowLayout {
            Layout.fillWidth: true
            Layout.leftMargin: 2
            spacing: 5

            PFLLabel {
                label: 'P'
                value: root.pr.pure
                color: appTheme.pure
            }

            PFLLabel {
                label: 'F'
                value: root.pr.far
                color: appTheme.far
            }

            PFLLabel {
                label: 'L'
                value: root.pr.lost
                color: appTheme.lost
            }
        }

        PFLLabel {
            Layout.fillWidth: true
            Layout.leftMargin: 2

            label: 'MR'
            value: root.pr.maxRecall
        }
    }
}
