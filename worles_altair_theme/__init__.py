import altair as alt

MARK_COLOR = '#202C59'
DARK_MARK_COLOR = '#3C54AC'

CATEGORY_COLORS = [
    MARK_COLOR,
    '#FEA82F',
    '#56876D',
    '#F26157',
    '#8B85C1',
    '#F19C79',
]

DARK_CATEGORY_COLORS = [
    DARK_MARK_COLOR,
    '#FEA82F',
    '#56876D',
    '#F26157',
    '#8B85C1',
    '#F19C79',
]

@alt.theme.register("worles", enable=True)
def worles() -> alt.theme.ThemeConfig:
    backgroundColor = '#F8F8F8'

    return {
        "config": {
            "view": {"continuousWidth": 300, "continuousHeight": 300},
            "mark": {
                "color": MARK_COLOR, 
                #"fill": markColor ,  
            },
            "legend":{'orient':'bottom'},
            'group':{'fill':backgroundColor},
            'background':backgroundColor,
            'title':{
                'anchor':'middle',
                'fontSize':20,
                'font':"Asap",
                'subtitleFontSize':13
            },
            "axis":{
                'titleFont':"Asap",
                'titleFontSize':14,
                'labelFontSize':12,
                'labelFont':'Asap'

            },
            'text':{
                'font':"Asap",
                'fontSize':14
            },
            'range':{'category':CATEGORY_COLORS},
            'legend':{'orient':'bottom',
                      'titleFont':"Asap", 'titleFontSize':14,
                      'labelFont':'Asap', 'labelFontSize':12

                      },
            'tooltip': {
                # Doesn't seem to be working
                'titleFont':"Asap", 
                'labelFont':'Asap', 
                'font':'Asap',
                #'labelFontSize':12
            }
        }
    }

@alt.theme.register("worles_minimal", enable=True)
def worles_minimal() -> alt.theme.ThemeConfig:

    backgroundColor= '#F8F8F8'


    return {
        "config": {
            "view": {"continuousWidth": 300, "continuousHeight": 300},
            "mark": {
                "color": MARK_COLOR,
            },
            "legend":{'orient':'bottom'},
            'group':{'fill':backgroundColor},
            'background':backgroundColor,
            'title':{
                'anchor':'middle',
                'fontSize':20,
                'font':"Asap",
                'subtitleFontSize':13
            },
            "axis":{
                'titleFont':"Asap",
                'titleFontSize':14,
                'labelFontSize':12,
                'labelFont':'Asap'
            },
            "axisY":{
                'grid': False
            },
            'text':{
                'font':"Asap",
                'fontSize':14
            },
            'range':{'category':CATEGORY_COLORS},
            'legend':{'orient':'bottom',
                      'titleFont':"Asap", 'titleFontSize':14,
                      'labelFont':'Asap', 'labelFontSize':12
                      },
            'tooltip': {
                'titleFont':"Asap",
                'labelFont':'Asap',
                'font':'Asap',
            }
        }
    }

@alt.theme.register("darkmode_worles", enable=True)
def darkmode_worles() -> alt.theme.ThemeConfig:

    backgroundColor= 'black'# '#FAFAFA'

    return {
        "config": {
            "view": {"continuousWidth": 300, "continuousHeight": 300},
            "mark": {
                "color": DARK_MARK_COLOR, 
            },
            "legend":{'orient':'bottom'},
            'group':{'fill':backgroundColor},
            'background':backgroundColor,
            'title':{
                'anchor':'middle',
                'fontSize':20,
                'font':"Roboto",
                'subtitleFontSize':13,
                'color':'white',
                'subtitleColor':'white'
            },
            "axis":{
                'titleFont':"Asap",
                'titleFontSize':14,
                'labelFontSize':12,
                'labelFont':'Asap',
                'labelColor':'white',
                'titleColor':'white',

            },
            'text':{
                'font':"Roboto",
                'fontSize':14,
                'fill':'white'
            },
            'range':{'category':DARK_CATEGORY_COLORS},
            'legend':{'orient':'bottom', 'textColor':'white',
                      'labelColor':'white', 'titleColor':'white',
                      'titleFont':"Asap", 'titleFontSize':14,
                      'labelFont':'Asap', 'labelFontSize':12
                      },
            'tooltip': {
                'titleFont':"Asap",
                'labelFont':'Asap',
                'font':'Asap',
            }
        }
    }
