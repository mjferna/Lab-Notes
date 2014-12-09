# Installing Ubuntu and Accessing Terminal on a Chromebook

**Introduction**

Browser-based laptops like the Google's Chromebook are becoming increasingly common, mainly because they are significantly cheaper than standard laptops or desktops. Although their low cost should enable more people to access computers, they lack some functionality out of the box. If you want to download Pandoc, for example, you'll need to install Ubuntu. This tutorial will transform a Chromebook into a fully functional laptop.

**Opening Crosh Shell in Chrome OS**

To open the Crosh Shell, press Ctrl+Alt+T. The Crosh shell will open in a browser tab.

The Crosh shell can be used for many purposes, including to connect to SSH servers, monitor resource usage, debug network problems, tweak hidden hardware settings, and perform hardware tests.

**Enabling Developer Mode**

To open full bash shell where you can run other Linux commands, you'll need to enable Developer Mode. Here are the steps.

Before you enable developer mode, make sure to back up all any locally saved data as this process clears the hard drive.

1. Put Chromebook into Recovery Mode. Hold the Escape and Refresh key, then press the Power button. Your Chromebook will reboot and display a giant yellow exclamation point if you're successful.

2. Next, press Control-D. A new screen with a red exclamation point will appear, asking you to press Enter to verify you want to continue with the process. After pressing Enter, and confirming you want to continue, don't do anything else. A few beeps and boops will come from the device, the screen will flash, and a countdown timer will display along the top of the screen.

3. Eventually your Chromebook will reboot, prompting you to complete the initial setup process again. You are now in Developer Mode. Every time you boot your device you will see a warning message reminding you disk verification is turned off (a feature of developer mode). Simply wait 30 seconds or so and your device will boot.

To access bash, open the terminal window and type shell.

**Installing Ubuntu**

You'll need [Crouton](https://goo.gl/fd3zc) to install Ubuntu. Make sure Crouton is in your Downloads folder.

Open bash and run the command:

```sh
sudo sh ~/Downloads/crouton -t kde
```

Note you can also run other desktop platforms, including Unity and Xfce. If you were to run Unity, then your command would look like this:

```sh
sudo sh ~/Downloads/crouton -t unity
```

The computer will now install Ubuntu. Depending on your connection, this will take awhile, usually around 15-30 minutes.

**Running Ubuntu**

Once installed, run this command in shell:

```sh
sudo startkde
```

If you installed Unity, then the command would be:

```sh
sudo startunity
```
You'll need to do this each time you start up your Chromebook.

To switch simultaneously between Chrome OS and Ubuntu, press Alt+Ctrl+Shift+Back and Alt+Ctrl+Shift+Forward

Pro-tip: The downloads folder is shared between both operating systems.
