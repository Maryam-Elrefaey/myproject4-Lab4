# 🛍️ Django Store Project (Lab 4)

This project is a **practice lab using Django** to build a simple online store app.  
It was developed as part of **Lab 4** requirements for learning Django models, queries, and media handling.  

## ✨ Features
### Models & Fields
- Product model with name, description, price, category, created/updated dates.  
- Image upload for each product (Media files).  
- Extra `Test` model to practice date & time fields.  

### Admin Integration
- Products can be added/edited through Django Admin panel.  

### QuerySet Methods (Examples)
- `filter` → products with price > 100  
- `exclude` → exclude cheap products  
- `order_by` → sort products by price (ascending/descending)  
- `exact` → find exact product name  
- `contains` → find products by keyword  
- `range` → filter products within price ranges  

### Templates
- Base layout + Home page + Store page.  
- Store page displays:  
  - All products  
  - Filtered products (expensive, range, etc.)  
  - Uploaded product images.  

## ⚙️ Tech Stack
- Django 5.x  
- SQLite (default)  
- Pillow (for image uploads)  
- HTML + CSS (basic templates with dark style)  

---

📌 **Goal**: A hands-on project to practice Django Models, QuerySets, Media Files, and connect them with Admin & Templates.  
