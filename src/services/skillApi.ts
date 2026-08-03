const API = "http://127.0.0.1:8000";

export async function getSkills() {
    const response = await fetch(`${API}/skills/`);
    return response.json();
}