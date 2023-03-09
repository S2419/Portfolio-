const websiteData = [
  {
    name: "Website 1",
    url: "https://www.website1.com",
    image: "website1.jpg"
  },
  {
    name: "Website 2",
    url: "https://www.website2.com",
    image: "website2.jpg"
  },
  {
    name: "Website 3",
    url: "https://www.website3.com",
    image: "website3.jpg"
  }
];

const websiteContainer = document.getElementById("website-container");

websiteData.forEach(function(website) {
  const websiteCard = document.createElement("div");
  websiteCard.classList.add("website-card");

  const websiteName = document.createElement("h2");
  websiteName.textContent = website.name;
  websiteCard.appendChild(websiteName);

  const websiteLink = document.createElement("a");
  websiteLink.href = website.url;
  websiteLink.textContent = website.url;
  websiteCard.appendChild(websiteLink);

  const websiteImage = document.createElement("img");
  websiteImage.src = website.image;
  websiteImage.alt = website.name;
  websiteCard.appendChild(websiteImage);

  websiteContainer.appendChild(websiteCard);
});
