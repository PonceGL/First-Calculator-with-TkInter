COLORS = {
    "blue": "#185ADB",
"white": "#ffffff",
"light_gray": "#EFEFEF",
"dark_blue": "#0A1931",
"yellow": "#FFC947",
"success": "#21E72C",
"warning": "#FF0000"
}



def on_enter(e):
    e.widget['bg'] = COLORS["blue"]
    e.widget['fg'] = COLORS["yellow"]

def on_leave(e):
    e.widget['bg'] = COLORS["dark_blue"]
    e.widget['fg'] = COLORS["light_gray"]