from django.shortcuts import render,redirect
from .db import db,myCollection,myCollection2,myUser
from django.http import HttpResponse
from bson.objectid import ObjectId
# Create your views here.

def home(req):
    users=[
        {"Name":"aaa","Age":21},
        {"Name":"bbb","Age":18},
        {"Name":"ccc","Age":16}
        ]

    return render(req,"index.html",context={"users":users})

def events(req):
    return render(req,"events.html")

def createProduct(req):
    # return render(req,"home.html")
    if req.method == "POST":        
        pName = req.POST.get("productName") 
        pPrice = req.POST.get("price")   
        pStock = req.POST.get("stock")    
    
        if pName and pPrice and pStock:
            data = {"productName": pName, "price": pPrice,"stock":pStock} 
            print(data,"data")       
            myCollection.insert_one(data)
            return redirect('productsList')
    
    return render(req, "home.html")

def viewProduct(req):
    try:
        getdatas = list(myCollection.find({}))
        # Convert _id (ObjectId) to string and rename
        for user in getdatas:
            user["id"] = str(user["_id"])  # Convert _id to string
        return render(req, "viewProducts.html", {"getdatas": getdatas})
    except Exception as e:
        print("Error:", e)
        return HttpResponse("An error occurred!!!")
    
def deleteProduct(req,id):
    try:
        myCollection.delete_one({"_id": ObjectId(id)})
        print(f"Deleted product with ID: {id}")  # Debugging
    except Exception as e:
        print("Error deleting product:", e)
    return redirect("productsList")

def editProduct(req,id):
    product = myCollection.find_one({"_id": ObjectId(id)})
    
    if req.method == "POST":
        # Retrieve updated data from the form
        updated_name = req.POST.get("productName")
        updated_price = req.POST.get("price")
        updated_stock = req.POST.get("stock")
        
        # Update the product in the database
        myCollection.update_one(
            {"_id": ObjectId(id)},
            {"$set": {"productName": updated_name, "price": updated_price, "stock": updated_stock}}
        )
        
        # Redirect back to the list of products after update
        return redirect('productsList')
    
    # If not a POST request, show the form with existing product data
    return render(req, 'edit.html', {'product': product})

def login(req):
    if req.method == "POST":
        userName = req.POST.get("name")
    
        userPassword = req.POST.get("password")

        print(userName,userPassword)

        user = myUser.find_one({"name":userName, "password":userPassword})
        print(user,"ischeck")
        if user:
            return redirect("productsList")
        else:
            return render(req,"login.html")
    return render(req, "login.html")