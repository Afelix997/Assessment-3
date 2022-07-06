document.getElementById('search-form').addEventListener('submit', (event)=>{
    event.preventDefault()

    const searchInput = document.getElementById('product')

    // send a GET request to /products on our server, passing searchInput.value as data.
    axios.get('/products', {params:{query: searchInput.value}})

    // handle the response from the server
        .then((response) => {
        
            if (searchInput.value == 'bait' || searchInput.value == 'fishing rods' || searchInput.value == 'fishing nets') {
                const inStock = document.createElement('h1')
                inStock.innerText = `That item is in stock!`
                document.body.appendChild(inStock)
            } else {
                newImage = document.createElement('img')
                newImage.src = response.data.url

                const soldOut = document.createElement('h1')
                soldOut.innerText = `Sorry, we don't offer any ${searchInput.value}s`

                const hr = document.createElement('hr')
                document.body.appendChild(newImage)
                document.body.appendChild(soldOut)
                document.body.appendChild(hr)

            }
        })
    // console.log(searchInput.value)
})