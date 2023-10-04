

# Product Requirements Documentation

**Summary**
| Field | Detail |
|-------|--------|
| Project Name | Shopping Cart|
| Developers | Bijay Kadariya |
| Live Website | Render |
| Repo | https://github.com/bijaykadariya123/capstone-Backend |
|List of Technologies | Python Django Neon

## Description
Shopping app will allow user to view the Item on collection. It will let users to Create, update and Delete .

## User Stories


- Users can see the site on desktop and mobile
- Users can create a new item
- Users can see all their items on the dashboard
- Users can update items
- User can delete items

## Route Tables


| Endpoint | Method | Response |
| -------- | ------ | -------- |
| /item | GET | JSON of all items|
| /item | POST | Create new item return JSON of new item | body must include data for new item |
| /item/:id | GET | JSON of item with matching id number | |
| /item/:id | PUT | update item with matching idea, return its JSON | body must include updated data |
| /item/:id | DELETE | delete the item with the matching id | 


## ERD (ENTITY RELATIONSHIP DIAGRAM)
[![](https://mermaid.ink/img/pako:eNplkDEKwzAMRa9iNOcEnrt06JTVixorjiGWjSIPIeTuNU6hhWj6PB7iSwdM2RNYIHlEDILJsWNjzLjkUiKHp1IyR0d9NpVGDWOiH-Sa3iSmSJzopmaJIfJN3gnl5saE4W_DlU7HMEAiSRh9q9rbONCFWgewLXqasa7qwPHZVKyax50nsCqVBqjFo9L3PrAzrluj5KNmeV3n9y-cH1CvVSE?type=png)](https://mermaid.live/edit#pako:eNplkDEKwzAMRa9iNOcEnrt06JTVixorjiGWjSIPIeTuNU6hhWj6PB7iSwdM2RNYIHlEDILJsWNjzLjkUiKHp1IyR0d9NpVGDWOiH-Sa3iSmSJzopmaJIfJN3gnl5saE4W_DlU7HMEAiSRh9q9rbONCFWgewLXqasa7qwPHZVKyax50nsCqVBqjFo9L3PrAzrluj5KNmeV3n9y-cH1CvVSE)

















