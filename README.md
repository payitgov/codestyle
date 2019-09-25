# IntelliJ

To use the IntelliJ code style, copy intellij.xml into `~/Library/Preferences/IdeaIC15/codestyles`,
restart IntelliJ, and select Payit Style in Preferences: `Editor -> Code Style -> Scheme`

## Checkstyle Plugin
1. `IntelliJ IDEA -> Preferences` or (`⌘,`)/(`CMD+,`).
2. `Plugins -> Marketplace -> CheckStyle-IDEA` and `Install`.
3. In the same preferences (`⌘,`) after the restart, at the bottom of the side-menu, go to `Other Settings -> Checkstyle`.
4. Click the `+` at the bottom of Configuration File:
   - Description: PayIt
   - Use a local Checkstyle file: [ Upload `checkstyle-idea.xml` ]
5. Check the active box for PayIt and hit `Apply -> OK`.

To use:
At the bottom of the IntelliJ IDE, you should see the CheckStyle tab (look for a red squiggly line).  Ensure that you have `PayIt` selected as the rule and use the buttons on the left to run CheckStyle.

# Gradle

To apply the checkstyle plugin in Gradle, add this line to your script, in an `allprojects` block if applicable: `apply from: 'https://bitbucket.org/paypit/codestyle/raw/master/checkstyle.gradle'`

This adds two tasks per project: `checkstyleMain` and `checkstyleTest`. These tasks also run when you run `build` or `check`.
