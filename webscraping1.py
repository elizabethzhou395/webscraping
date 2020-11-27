from bs4 import BeautifulSoup
import re
import requests
import pandas as pd
import numpy as np

# catalogueHTML = requests.get("http://books.toscrape.com/").text
# catalogueSoup = BeautifulSoup(catalogueHTML, 'catalogueHTML.parser')

bookTitles = []
bookPrices = []
rating = []
category = []

for i in range(1):

    catalogueURL = "http://books.toscrape.com/catalogue/page-{}.html".format(i+1)

    catalogueHTML = requests.get(catalogueURL).text
    catalogueSoup = BeautifulSoup(catalogueHTML,'html.parser')

    #finding table with the list of books
    pageInsideHeading = catalogueSoup.find("div",{"id": 'messages'})
    pageHeading = pageInsideHeading.parent
    bookSection = pageHeading.findNext("section")
    bookDiv = bookSection.findNext("div").findNext("div")
    #finding row with the books
    bookRow = bookDiv.findNext("ol")
    #finding the list of books under the ol tag
    bookList = bookRow.find_all('li')

    #finding out category list
    pageTitle = catalogueSoup.find("body",{"id": 'default'})
    categoryRow = pageTitle.findNext("div").findNext("div").findNext("div").findNext("div").findNext("div").findNext("aside")
    categoryDiv = categoryRow.findNext("div")
    categoryList = categoryDiv.findNext("ul").findNext("li").findNext("ul")
    
    # print(categoryList)
    
    #iterate through each item in the book list
    for bookItem in bookList:
        #get the title of the book
        bookItemName = bookItem.findNext("a").findNext("a")
        bookTitle = bookItemName.get('title')
        #store the bookTitles in an array
        bookTitles.append(bookTitle)
        print(bookTitle)

        #get the price of the book
        bookPriceSection = bookItem.findNext("div").findNext("div")
        bookPriceTag = bookPriceSection.findNext("p")
        #scraping text inside a p tag
        bookPrice = bookPriceTag.text
        #store the book prices in an array
        bookPrices.append(bookPrice)

        #get the rating of book
        bookRatingLocation = bookItem.findNext("p")
        #converting the catalogueHTML into a string
        bookRatingString = str(bookRatingLocation)
        bookRatingPart = (bookRatingString.split(' '))[2]
        bookRating = bookRatingPart.split("\">")[0]
        #store ratings in an array
        rating.append(bookRating)

        # for categoryItem in categoryList:
        categoryNameString = str(categoryList.findNext("a"))
        categoryNamePart = categoryNameString.split('/')[2]
        categoryName = categoryNamePart.split('_')[0]
        print(categoryName)

        
    
    
    
    # #find a way to iterate through each catalogueHTML and find if bookTitle is located in each catalogueHTML list.
    # for categoryItem in categoryList:
        # categoryNameString = str(categoryItem.findNext("a"))
        # categoryNamePart = categoryNameString.split('/')[2]
        # categoryName = categoryNamePart.split('_')[0]
    #         # categoryPage = categoryNamePart.split('_')[1]
    #     categoryURL = "https://books.toscrape.com/catalogue/category/books/{}_{}/index.html".format(categoryName, i+2)
    #     print(categoryURL)
    #     categoryHTML = requests.get(categoryURL).text
    #     categorySoup = BeautifulSoup(categoryHTML,'html.parser')
    #     pageInsideHeadingCat = categorySoup.find("div",{"id": 'messages'})
    #     # print(pageOverView)
    #     pageHeadingCat = pageInsideHeadingCat.parent
    #     bookSectionCat = pageHeadingCat.findNext("section")
    #     bookDivCat = bookSectionCat.findNext("div").findNext("div")
    #     #finding row with the books
    #     bookRowCat = bookDivCat.findNext("ol")
    #     #finding the list of books under the ol tag
    #     bookListCat = bookRowCat.find_all('li')
        # for bookItemCat in bookListCat:
        #     bookItemNameCat = bookItemCat.findNext("a").findNext("a")
        #     bookTitleCat = bookItemNameCat.get('title')
        #     if (bookTitle == bookTitleCat):
        #         print(bookTitle, categoryName)
        
        # if (bookTitle == categorySoup.find('title')):
        #     print(bookTitle, categoryName)
        

# #transfer lists into a dataframe
# books = pd.DataFrame({
#     'Title': bookTitles,
#     'Price': bookPrices,
#     'Rating': rating,
# })
# #convert dataframe to csv file
# books.to_csv('books.csv')
