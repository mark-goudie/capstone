// Function to get CSRF token from cookies
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function toggleLike(postId) {
  const likeHeart = document.getElementById(`like-heart-${postId}`);
  const isLiked = likeHeart.getAttribute("data-liked") === "true";

  fetch(`/like/${postId}`, {
    method: "POST",
    headers: {
      "X-CSRFToken": getCookie("csrftoken"),
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      like: !isLiked,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.liked) {
        likeHeart.classList.add("liked");
        likeHeart.classList.remove("unliked");
        likeHeart.setAttribute("data-liked", "true");
      } else {
        likeHeart.classList.add("unliked");
        likeHeart.classList.remove("liked");
        likeHeart.setAttribute("data-liked", "false");
      }
      likeHeart.nextElementSibling.textContent = data.likes;
    })
    .catch((error) => console.log(error));
}
