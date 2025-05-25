import altair as alt

@alt.theme.register("worles", enable=True)
def worles() -> alt.theme.ThemeConfig:
    markColor = '#202C59'
    backgroundColor= '#F8F8F8'# '#FAFAFA'

    categoryColors = [
        markColor,
        '#FEA82F',
        '#56876D',
        '#F26157',
        '#8B85C1',
        '#F19C79',
    ]
#    cColors = ["a82431","f5a6e6","8d80c7","2559a7","ff934f","6cae75",'49848E','60B2E5']
#    cColors = ['#'+c for c in cColors]

    return {
        "config": {
            "view": {"continuousWidth": 300, "continuousHeight": 300},
            "mark": {
                "color": markColor, 
                #"fill": markColor ,  
            },
            "legend":{'orient':'bottom'},
            'group':{'fill':backgroundColor},
            'background':backgroundColor,
            'title':{
                'anchor':'start',
                'fontSize':20,
                'font':"Roboto",
                'subtitleFontSize':13
            },
            "axis":{
                'titleFont':"Asap Condensed",
                'titleFontSize':14,
                'labelFontSize':12,
                'labelFont':'Asap Condensed'

            },
            'text':{
                'font':"Roboto",
                'fontSize':14
            },
            'range':{'category':categoryColors},
            'legend':{'orient':'bottom',
                      'titleFont':"Asap Condensed", 'titleFontSize':14,
                      'labelFont':'Asap Condensed', 'labelFontSize':12

                      },
            'tooltip': {
                # Doesn't seem to be working
                'titleFont':"Asap Condensed", 
                'labelFont':'Asap Condensed', 
                'font':'Asap Condensed',
                #'labelFontSize':12
            }
        }
    }

@alt.theme.register("darkmode_worles", enable=True)
def darkmode_worles() -> alt.theme.ThemeConfig:
    markColor = '#3C54AC'
    backgroundColor= 'black'# '#FAFAFA'

    categoryColors = [
        markColor,
        '#FEA82F',
        '#56876D',
        '#F26157',
        '#8B85C1',
        '#F19C79',
    ]
#    cColors = ["a82431","f5a6e6","8d80c7","2559a7","ff934f","6cae75",'49848E','60B2E5']
#    cColors = ['#'+c for c in cColors]

    return {
        "config": {
            "view": {"continuousWidth": 300, "continuousHeight": 300},
            "mark": {
                "color": markColor, 
                #"fill": markColor ,  
            },
            "legend":{'orient':'bottom'},
            'group':{'fill':backgroundColor},
            'background':backgroundColor,
            'title':{
                'anchor':'start',
                'fontSize':20,
                'font':"Roboto",
                'subtitleFontSize':13,
                'color':'white',
                'subtitleColor':'white'
            },
            "axis":{
                'titleFont':"Asap Condensed",
                'titleFontSize':14,
                'labelFontSize':12,
                'labelFont':'Asap Condensed',
                'labelColor':'white',
                'titleColor':'white',

            },
            'text':{
                'font':"Roboto",
                'fontSize':14,
                'fill':'white'
            },
            'range':{'category':categoryColors},
            'legend':{'orient':'bottom', 'textColor':'white',
                      'labelColor':'white', 'titleColor':'white',
                      'titleFont':"Asap Condensed", 'titleFontSize':14,
                      'labelFont':'Asap Condensed', 'labelFontSize':12
                      }
        }
    }
