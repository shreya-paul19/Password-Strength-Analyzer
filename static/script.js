async function checkStrength() {

    const password =
        document.getElementById("password").value;

    const response = await fetch("/analyze", {
        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            password: password
        })
    });

    const data = await response.json();

    const bar =
        document.getElementById("strength-bar");

    const result =
        document.getElementById("result");

    const entropy =
        document.getElementById("entropy");

    const crackTime =
        document.getElementById("crack-time");

    const warning =
        document.getElementById("warning");

    const breachWarning =
        document.getElementById("breach-warning");

    const policyList =
        document.getElementById("policy-list");

    bar.style.width = data.score + "%";

    if (data.strength === "Weak") {

        bar.style.background = "red";

    }
    else if (data.strength === "Medium") {

        bar.style.background = "orange";

    }
    else {

        bar.style.background = "lime";
    }

    result.innerHTML =
        `Strength: ${data.strength} (${data.score}/100)`;

    entropy.innerHTML =
        `Entropy: ${data.entropy} bits`;

    crackTime.innerHTML =
        `Estimated Crack Time: ${data.crack_time}`;

    if (data.common) {

        warning.innerHTML =
            "⚠ Warning: This is a commonly used password!";

        warning.style.color = "#ff4d4d";
        warning.style.fontWeight = "bold";

    }
    else {

        warning.innerHTML = "";
    }

    if (data.breach && data.breach.breached) {

        breachWarning.innerHTML =
            `🚨 Found in ${data.breach.count.toLocaleString()} known breaches`;

        breachWarning.style.color = "#ff4d4d";
        breachWarning.style.fontWeight = "bold";

    }
    else {

        breachWarning.innerHTML =
            "✅ Not found in known breaches";

        breachWarning.style.color = "#00ff88";
        breachWarning.style.fontWeight = "bold";
    }

    let policy = data.policy;

    policyList.innerHTML = `
        <li>${policy.length ? '✅' : '❌'} Minimum 12 Characters</li>
        <li>${policy.uppercase ? '✅' : '❌'} Uppercase Letter</li>
        <li>${policy.lowercase ? '✅' : '❌'} Lowercase Letter</li>
        <li>${policy.number ? '✅' : '❌'} Number</li>
        <li>${policy.special ? '✅' : '❌'} Special Character</li>
    `;
}

async function generatePassword() {

    const response =
        await fetch('/generate');

    const data =
        await response.json();

    document.getElementById(
        "generated-password"
    ).innerHTML = data.password;
}

function togglePassword() {

    const passwordField =
        document.getElementById("password");

    const button =
        document.getElementById("toggle-btn");

    if (passwordField.type === "password") {

        passwordField.type = "text";
        button.innerHTML = "🙈 Hide";

    }
    else {

        passwordField.type = "password";
        button.innerHTML = "👁 Show";
    }
}