<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>922</width>
    <height>627</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QGridLayout" name="gridLayout">
    <item row="0" column="0">
     <layout class="QHBoxLayout" name="horizontalLayout">
      <item>
       <widget class="QSplitter" name="splitter">
        <property name="orientation">
         <enum>Qt::Vertical</enum>
        </property>
        <widget class="QLabel" name="label">
         <property name="text">
          <string>TextLabel</string>
         </property>
        </widget>
        <widget class="QWidget" name="">
         <layout class="QHBoxLayout" name="horizontalLayout_2">
          <item>
           <widget class="QPushButton" name="pushButton_5">
            <property name="sizePolicy">
             <sizepolicy hsizetype="Expanding" vsizetype="Fixed">
              <horstretch>0</horstretch>
              <verstretch>0</verstretch>
             </sizepolicy>
            </property>
            <property name="text">
             <string>Prev Doc</string>
            </property>
            <property name="icon">
             <iconset>
              <normaloff>images/Prev-File.png</normaloff>images/Prev-File.png</iconset>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="pushButton_7">
            <property name="sizePolicy">
             <sizepolicy hsizetype="Minimum" vsizetype="Fixed">
              <horstretch>0</horstretch>
              <verstretch>0</verstretch>
             </sizepolicy>
            </property>
            <property name="text">
             <string>Zoom -</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="pushButton_3">
            <property name="sizePolicy">
             <sizepolicy hsizetype="Expanding" vsizetype="Fixed">
              <horstretch>0</horstretch>
              <verstretch>0</verstretch>
             </sizepolicy>
            </property>
            <property name="text">
             <string/>
            </property>
            <property name="icon">
             <iconset>
              <normaloff>images/Prev-Page.png</normaloff>images/Prev-Page.png</iconset>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="pushButton_2">
            <property name="sizePolicy">
             <sizepolicy hsizetype="Expanding" vsizetype="Fixed">
              <horstretch>0</horstretch>
              <verstretch>0</verstretch>
             </sizepolicy>
            </property>
            <property name="text">
             <string/>
            </property>
            <property name="icon">
             <iconset>
              <normaloff>images/Next-Page.png</normaloff>images/Next-Page.png</iconset>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="pushButton_6">
            <property name="sizePolicy">
             <sizepolicy hsizetype="Minimum" vsizetype="Fixed">
              <horstretch>0</horstretch>
              <verstretch>0</verstretch>
             </sizepolicy>
            </property>
            <property name="text">
             <string>Zoom +</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="pushButton_4">
            <property name="sizePolicy">
             <sizepolicy hsizetype="Minimum" vsizetype="Fixed">
              <horstretch>0</horstretch>
              <verstretch>0</verstretch>
             </sizepolicy>
            </property>
            <property name="text">
             <string>Next Doc</string>
            </property>
            <property name="icon">
             <iconset>
              <normaloff>images/Next-File.png</normaloff>images/Next-File.png</iconset>
            </property>
           </widget>
          </item>
         </layout>
        </widget>
       </widget>
      </item>
      <item>
       <widget class="QSplitter" name="splitter_3">
        <property name="orientation">
         <enum>Qt::Vertical</enum>
        </property>
        <widget class="QLabel" name="label_2">
         <property name="font">
          <font>
           <pointsize>14</pointsize>
          </font>
         </property>
         <property name="text">
          <string>Image ID : CALOSA-2019_01007271</string>
         </property>
        </widget>
        <widget class="QLabel" name="label_4">
         <property name="text">
          <string>Full Legal Extract</string>
         </property>
        </widget>
        <widget class="QLineEdit" name="lineEdit"/>
        <widget class="QSplitter" name="splitter_2">
         <property name="orientation">
          <enum>Qt::Horizontal</enum>
         </property>
         <widget class="QLabel" name="label_3">
          <property name="text">
           <string>Is full legal Extracted ?</string>
          </property>
         </widget>
         <widget class="QComboBox" name="comboBox">
          <property name="sizePolicy">
           <sizepolicy hsizetype="Minimum" vsizetype="Fixed">
            <horstretch>0</horstretch>
            <verstretch>0</verstretch>
           </sizepolicy>
          </property>
          <item>
           <property name="text">
            <string>YES</string>
           </property>
          </item>
          <item>
           <property name="text">
            <string>NO</string>
           </property>
          </item>
         </widget>
        </widget>
        <widget class="QLabel" name="label_5">
         <property name="text">
          <string>Remark</string>
         </property>
        </widget>
        <widget class="QLineEdit" name="lineEdit_2"/>
        <widget class="QPushButton" name="pushButton">
         <property name="text">
          <string>Submit</string>
         </property>
        </widget>
       </widget>
      </item>
     </layout>
    </item>
   </layout>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>922</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
