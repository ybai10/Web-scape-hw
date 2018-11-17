{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, render_template, redirect\n",
    "from flask_pymongo import PyMongo\n",
    "import scrape_mars\n",
    "\n",
    "# Create an instance of Flask\n",
    "app = Flask(__name__)\n",
    "# Use PyMongo to establish Mongo connection, set inline\n",
    "mongo = PyMongo(app, uri=\"mongodb://localhost:27017/mars_hw\")\n",
    "\n",
    "# Route to render index.html template using data from Mongo\n",
    "@app.route('/')\n",
    "def index():\n",
    "    # Find one record of data from the mongo databas\n",
    "    mars = mongo.db.mars.find_one()\n",
    "    # Return template and data\n",
    "    return render_template('index.html', mars=mars)\n",
    "\n",
    "# Route that will trigger the scrape function\n",
    "@app.route('/scrape')\n",
    "def scrape():\n",
    "    \n",
    "    \n",
    "    # Run the scrape function\n",
    "    table = scrape_mars.scrape()\n",
    "    mongo.db.collection.update({}, mars_data, upsert=True)\n",
    "    \n",
    "    return redirect(\"/\", code=302)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
