
from frontend.models import *
from core.manifest import COMPANY_DETAILS


services = [
    {
        'icon':"",
        'title': "Professionl IT Training",
        'description':"""
Sharashell offers comprehensive professional IT training programs 
designed to enhance skills and knowledge in various IT domains.
        """
    },

    {
        'icon':"",
        'title': "Data Analysis Projects",
        'description':"""
Sharashell provides specialized services in data analysis, helping organizations 
to make sense of their data and derive actionable insights.
        """
    },
    {
        'icon':"",
        'title': "Portal/Websites Designs",
        'description':"""
        We  offers professional portal and website design services, 
        creating visually appealing and user-friendly digital platforms.
        """
    },
    {
        'icon':"",
        'title': "Mobile Application Development",
        'description':"""
        Sharashell specializes in developing high-quality mobile applications for both Android and iOS platforms.
        """
    },
    {
        'icon':"",
        'title': "Organizational Software Management",
        'description':"""
        Sharashell provides comprehensive organizational software management services designed to streamline 
        business processes and enhance operational efficiency.
        """
    },
    {
        'icon':"",
        'title': "Cloud Computing",
        'description':"""
        Sharashell offers cloud computing services that enable businesses to leverage the power 
        of the cloud for their IT infrastructure needs.
        """
    },
]


teams = [
    {
        'name':"",
        'position':'',
        'short_descriptions':''
    },
]



def frontendContext(request):
    context = {}
    context["company"]=COMPANY_DETAILS
    return context