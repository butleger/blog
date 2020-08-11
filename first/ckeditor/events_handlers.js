

addEventListener("DOMContentLoaded", () => {
    let articles = document.getElementByClassName("articles")
    for (article of articles)
    {
        article.addEventListener("onclick" () => {
            window.location.href = "/articles/" + {{ title }} + "/"
        })
    }
})

