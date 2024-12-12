// Scroll to a specific section
function scrollToSection(sectionId) {
    const section = document.getElementById(sectionId);
    if (section) {
        section.scrollIntoView({ behavior: "smooth" });
    }
}

// Simulate a login button click
document.getElementById("login-btn").addEventListener("click", function () {
    alert("Login functionality coming soon!");
});
