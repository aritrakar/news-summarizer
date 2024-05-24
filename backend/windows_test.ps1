$headers = @{
    "Content-Type" = "application/json"
}

$body = @{
    # url = "https://www.nbcnews.com/business/business-news/ticketmaster-live-nation-lawsuit-mean-fans-live-music-rcna153739"
    url = "https://www.cbsnews.com/news/senate-border-security-bill-vote/"
}

$response = Invoke-RestMethod -Uri "http://localhost:5000/summarize" -Method Post -Headers $headers -Body ($body | ConvertTo-Json)

$response | ConvertTo-Json
