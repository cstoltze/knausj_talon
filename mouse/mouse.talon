not tag: user.full_mouse_grid_showing
and not mode: sleep
not tag: user.shotbox_showing
and not mode: sleep
-

# TODO:
# - need a generic for any clicking zoom overlay to trigger the click

###
# Configuration
###
mouse sleep: user.mouse_sleep()
# sometimes the tobii stops tracking when awake, and triggering wake again won't fix it
mouse wake:
    user.mouse_sleep()
    user.mouse_wake()
mouse control: user.mouse_toggle_control_mouse()
(mouse | run) calibration: user.mouse_calibrate()
[(enable | disable)] zoom mouse: user.mouse_toggle_zoom_mouse()
[(enable | disable)] auto click: user.mouse_toggle_zoom_auto_click()
[(enable | disable)] blink click: user.mouse_toggle_blink_click()
[(enable | disable)] sleep tracker: user.mouse_toggle_eye_mouse_sleep_tracker()

###
# General clicking and movement
###
# single click
[mouse] click: user.mouse_click(0, 1)
# right click
[mouse] (ricky | right click): user.mouse_click(1, 1)
## middle click
[mouse] middle click: user.mouse_click(2, 1)
## double click
[mouse] double click: user.mouse_click(0, 2)
## triple click
[mouse] triple click: user.mouse_click(0, 3)

mouse hover: user.mouse_move_cursor()

# XXX - This should detective we are in zoom mode
mouse drag: user.mouse_drag(0)
<user.modifiers> mouse drag:
    key("{modifiers}:down")
    user.mouse_click(0, 1)

    key("{modifiers}:up")

#see keys.py for modifiers.
#defaults
#command
#control
#option = alt
#shift
#super = windows key

<user.modifiers> click:
    key("{modifiers}:down")
    user.mouse_click(0, 1)
    key("{modifiers}:up")

###
# Scrolling and dragging
###
wheel down: user.mouse_scroll_down()
wheel tiny [down]: mouse_scroll(20)
# NOTE: can be repeated for faster scrolling
wheel downer: user.mouse_scroll_down_continuous()

wheel up: user.mouse_scroll_up()
wheel tiny up: mouse_scroll(-20)
# NOTE: can be repeated for faster scrolling
wheel upper: user.mouse_scroll_up_continuous()

# NOTE: can be repeated to stop gaze scroll
wheel gaze: user.mouse_gaze_scroll()

wheel stop: user.mouse_scroll_stop()
wheel left: mouse_scroll(0, -40)
wheel tiny left: mouse_scroll(0, -20)
wheel right: mouse_scroll(0, 40)
wheel tiny right: mouse_scroll(0, 20)

curse (show | yes): user.mouse_show_cursor()
curse (hide | no): user.mouse_hide_cursor()

# see mouse_zoomed.talon
#left drag | drag:
#    user.mouse_drag(0)
#    # close the mouse grid
#    user.grid_close()
#right drag | righty drag:
#    user.mouse_drag(1)
#    # close the mouse grid
#    user.grid_close()
#end drag | drag end:
#    user.mouse_drag_end()

###
# Coordinate capturing
###
mouse trap: user.mouse_capture_coordinates()
log mouse clicks: user.mouse_log_clicks()

###
# Zoom features
###
# disables zoom without clicking in case it fails
cancel zoom: user.mouse_cancel_zoom_mouse()

# zoom single click - auto clicks if enabled
#(kiff|eagle): user.mouse_zoom_single_click()
#eagle: user.mouse_zoom_single_click()

# zoom single click - auto click even if autoclick setting disabled
#kick: user.mouse_zoom_auto_single_click()

# relocate cursor to clicked location
zoom portal: user.mouse_zoom_move_cursor()

# auto relocate cursor to clicked location
auto portal: user.mouse_zoom_auto_move_cursor()
