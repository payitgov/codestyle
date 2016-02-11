# IntelliJ

To use the IntelliJ code style, copy intellij.xml into `~/Library/Preferences/IdeaIC15/codestyles`,
restart IntelliJ, and select Payit Style in Preferences: `Editor -> Code Style -> Scheme`

# Gradle

To apply the checkstyle plugin in Gradle, add this line to your script, in an `allprojects` block if applicable: `apply from: 'https://bitbucket.org/paypit/codestyle/raw/master/checkstyle.gradle'`

This adds two tasks per project: `checkstyleMain` and `checkstyleTest`. These tasks also run when you run `build` or `check`.