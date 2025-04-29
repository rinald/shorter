const API_URL = import.meta.env.PROD ? "/api" : "http://localhost:8000";

const createShortUrl = async (longUrl: string) => {
  const response = await fetch(`${API_URL}/shorten`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ long_url: longUrl }),
  });

  return response.json();
};

const redirect = async (shortUrl: string) => {
  const response = await fetch(`${API_URL}/url/${shortUrl}`);
  if (!response.ok) {
    throw new Error(`Failed to redirect: ${response.status}`);
  }

  return response;
};

export { createShortUrl, redirect };
