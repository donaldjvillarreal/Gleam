//https://www.hacksplaining.com/prevention/click-jacking

if (self == top) {
    // Everything checks out, show the page.
    document.documentElement.style.display = 'block';
} else {
    // Break out of the frame.
    top.location = self.location;
}