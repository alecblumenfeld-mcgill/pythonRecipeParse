import os, sys,json
import subprocess as sub
from settings_local import *
from parse_rest.connection import register
from parse_rest.datatypes import Object
import ParsePy
import re

auth =getAuthKeys()
ParsePy.APPLICATION_ID = auth[0]
ParsePy.MASTER_KEY = auth[2]

def requestRecipe(url):
    try:
        cmd = "parser/bin/parse_recipe {0} json".format(url)
        output =  sub.Popen(cmd,stdout=sub.PIPE,stderr=sub.PIPE, shell=True)
        lines_iterator = iter(output.stdout.readline, b"")
        output_String =""
        for line in lines_iterator:
            output_String += line # yield line
        toret = json.loads(output_String)
        return toret
    except Exception, e:
        return e
    else:
        pass
   

   
class Recipe(object):
    """docstring for Recipie"""
    def __init__(self, url):
        super(Recipe, self).__init__()
        self.parseObject = ParsePy.ParseObject("ImportedRecipes")
        self.recipeJSON = requestRecipe(url)
        self.parseObject.title = requestRecipe(url)["title"]
        self.parseObject.directions = self.recipeJSON["instructions"][0]["list"]
        self.parseObject.ingredients = self.recipeJSON["ingredients"][0]["list"]
        self.parseObject.photo = self.recipeJSON["photo_url"]
        self.parseObject.recipeUrl = self.recipeJSON["url"]
        self.parseObject.credit = self.recipeJSON["credits"]

    def save(self):
        self.parseObject.save()
        pass
        # self.parseObject.coverImage = self.recipeJSON["title"]



if __name__ == '__main__':

    newRecipe = Recipe("http://www.bonappetit.com/recipe/no-bake-chocolate-cream-pie-with-toasted-meringue")
    newRecipe.parseObject.save()
