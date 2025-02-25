import streamlit as st
import soco

st.title("Sonos Volume Controller")


def build_ui(speakers):
    for speaker in speakers:
        st.subheader(speaker.player_name)

        volume_key = f"volume_{speaker.uid}"

        if volume_key not in st.session_state:
            st.session_state[volume_key] = speaker.volume

        def update_volume(speaker=speaker, key=volume_key):
            speaker.volume = st.session_state[key]
            st.success(
                f"Updated {speaker.player_name} volume to {st.session_state[key]}"
            )

        st.slider(
            f"Volume for {speaker.player_name}",
            min_value=0,
            max_value=50,
            value=st.session_state[volume_key],
            key=volume_key,
            on_change=update_volume,
        )


def main():
    speakers = list(soco.discover() or [])

    if not speakers:
        return st.error("No Sonos speakers found on the network.")

    build_ui(speakers)


if __name__ == "__main__":
    main()
