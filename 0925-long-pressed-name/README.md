<h2><a href="https://leetcode.com/problems/long-pressed-name/">925. Long Pressed Name</a></h2><h3>Easy</h3><hr><div><p><font papago-translate="cached" papago-id="16">Your friend is typing his </font><code>name</code><font papago-translate="cached" papago-id="17"> into a keyboard. Sometimes, when typing a character </font><code>c</code></p>

<p><font papago-translate="cached" papago-id="19">You examine the </font><code>typed</code><font papago-translate="cached" papago-id="20"> characters of the keyboard. Return </font><code>True</code><font papago-translate="cached" papago-id="21"> if it is possible that it was your friends name, with some characters (possibly none) being long pressed.</font></p>

<p>&nbsp;</p>
<p><strong class="example" papago-id="22" papago-translate="translated">Example 1:</strong></p>

<pre papago-id="23" papago-translate="cached"><strong papago-id="23-0">Input:</strong> name = "alex", typed = "aaleex"
<strong papago-id="23-2">Output:</strong> true
<strong papago-id="23-4">Explanation: </strong>'a' and 'e' in 'alex' were long pressed.
</pre>

<p><strong class="example" papago-id="24" papago-translate="translated">Example 2:</strong></p>

<pre papago-id="25" papago-translate="cached"><strong papago-id="25-0">Input:</strong> name = "saeed", typed = "ssaaedd"
<strong papago-id="25-2">Output:</strong> false
<strong papago-id="25-4">Explanation: </strong>'e' must have been pressed twice, but it was not in the typed output.
</pre>

<p>&nbsp;</p>
<p><strong papago-id="26" papago-translate="translated">Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= name.length, typed.length &lt;= 1000</code></li>
	<li><code>name</code><font papago-translate="cached" papago-id="27"> and </font><code>typed</code><font papago-translate="cached" papago-id="28"> consist of only lowercase English letters.</font></li>
</ul>
</div>