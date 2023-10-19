# LeetCode Problem Collection

Welcome to my collection of LeetCode problems! This repository is designed to help me improve my coding skills by providing solutions to a variety of LeetCode problems. You, the reader, might find it helpful because it contains a collection of the most asked problems during interviews.

![Logo-leetcode](img/leetcode.png)
## Accessing LeetCode Problems in Visual Studio Code

To make the most of this collection, you can access LeetCode problems directly within Visual Studio Code using the LeetCode plugin. Here's a step-by-step guide on how to set it up:

1. **Log in to LeetCode:**
   Visit [leetcode.com](https://leetcode.com/) and log in to your account.

2. **Opening Developer Tools:**
   - Once logged in, navigate to any page on the LeetCode website.
   - Right-click anywhere on the page and select 'Inspect' from the context menu. This will open the browser's developer tools.

3. **Using the Network Tab:**
   - In the developer tools, locate and click on the 'Network' tab. If you can't see it, it might be under the '>>' symbol or in a dropdown menu.
   - From the available options, choose 'Fetch' or 'XHR' to filter the network requests.

4. **Selecting a Graphql Request:**
   - Look through the list of network requests and select any request with 'graphql' in its name. These are the requests that the LeetCode plugin uses to fetch data.

5. **Copying Cookies:**
   - Within the selected request details, go to the 'Headers' section.
   - Scroll down until you find the 'Cookie' header. This header contains the necessary authentication information.
   - Copy the entire content of the 'Cookie' header.

6. **Configuring the VS Code Plugin:**
   - Open Visual Studio Code.
   - If you haven't already, install the [LeetCode plugin](https://marketplace.visualstudio.com/items?itemName=shengchen.vscode-leetcode) from the Visual Studio Code Marketplace.
   - In the LeetCode plugin settings, find the option to provide your LeetCode account information.
   - Paste the previously copied 'Cookie' information in the appropriate field, along with your email.

Now you're all set to use the LeetCode plugin within Visual Studio Code to access problems, submit solutions, and track your progress.

Feel free to explore the problem collection in this repository and use the provided solutions to enhance your coding skills. Happy coding!
