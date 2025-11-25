Audio Processor and 8ch Amplifier with CamillaDSP on RADXA CM3J board

Это мой крайний РАБОТАЮЩИЙ проект автомобильного процессорного усилителя 
Проект состоит из проекта KiCAD, проекта корпуса FreeCAD и набора софта для запуска в работу.

Железо: 
Вычислитель - одноплатный компьютер Radxa CM3J в формфакторе Raspberry Pi CM4 на чипе RK3568, 2gB RAM, 8gB EMMC, WiFi. 
Усилитель - две микросхемы TAS6424-Q1, 4-хканальные усилители со входом I2S, суммарная мощность 8х50 Вт. 
Аналоговый вход - АЦП PCM1808, аналоговый выход - ЦАП PCM5102A. Аппаратоно-программный энкодер для регулировки громкости. 
Блок питания - преобразователь с бортового автомобильного в 25В однополярного напряжения со стаблизацией. 
Все помещено корпус из алюминия.

Софт: ОС Armbian, модифицировано дерево устройств. 
Обработка заука - СamillaDSP, плеер - mpd, приемник DLNA - upmpdcli, приемник USB - g_audio (виртуальный гаджет, частота дискретизации до 192 КГц), 
набор скриптов для инициализации усилителей, управления питанием, энкодером и т.д.

Проект выкладывается как есть. Любой желающий может его скачать, заказать платы, спаять и запустить в работу.

С документацией плохо, нужно время.

Небольшое описание проекта на Драйве: https://www.drive2.ru/b/716015167221021455/

Группа для обсуждения: https://t.me/DigitalAudioWare

Виктор Хомченко https://t.me/mikhalych24 Красноярск 2025г.


EN:

Audio processor and 8-channel amplifier with CamillaDSP on a RADXA CM3J board

This is my last WORKING automotive processor amplifier project. 
The project consists of a project in KiCad, a case project in FreeCAD, and a set of startup software.

Hardware: Radxa CM3J single—board computer in Raspberry Pi CM4 form factor on RK3568 chip, 2 GB RAM, 8 GB EMMC, WiFi. 
Amplifier — two TAS6424-Q1 chips, 4-channel amplifiers with I2S input, total power 8x50 watts. 
The analog input is the PCM1808 ADC, the analog output is the PCM5102A DAC. 
A hardware-software encoder for volume control. 
The power supply unit is a converter of on—board automotive voltage to a unipolar voltage of 25 V with stabilization. 
Everything is housed in an aluminum case.

Software: Armbian OS, modified device tree. Sound processing — CamillaDSP, MPD player, DLNA receiver — upmpdcli, 
USB receiver — g_audio (virtual gadget, sampling rate up to 192 kHz), 
a set of scripts for initializing amplifiers, power management, encoder, etc.

The project is laid out as it is. Anyone can download it, order the boards, solder it and put it into operation.

There are problems with the documentation, it takes time.

A brief description of the project on Drive2: https://www.drive2.ru/b/716015167221021455/

The discussion group: https://t.me/DigitalAudioWare

Viktor Khomchenko https://t.me/mikhalych24 Krasnoyarsk, 2025
