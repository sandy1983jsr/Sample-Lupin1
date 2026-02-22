KeyError: This app has encountered an error. The original error message is redacted to prevent data leaks. Full error details have been recorded in the logs (if you're on Streamlit Cloud, click on 'Manage app' in the lower right of your app).
Traceback:
File "/mount/src/sample-lupin1/green_ops_control_tower/app.py", line 4, in <module>
    from pages import landing, plant, boiler, dryer
File "/mount/src/sample-lupin1/green_ops_control_tower/pages/landing.py", line 5, in <module>
    corp = st.session_state["corporate_kpis"]
           ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/state/session_state_proxy.py", line 101, in __getitem__
    return get_session_state()[key]
           ~~~~~~~~~~~~~~~~~~~^^^^^
File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/state/safe_session_state.py", line 104, in __getitem__
    return self._state[key]
           ~~~~~~~~~~~^^^^^
File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/state/session_state.py", line 486, in __getitem__
    raise KeyError(_missing_key_error_message(key))
