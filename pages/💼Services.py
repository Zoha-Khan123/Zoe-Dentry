import streamlit as st
st.set_page_config(page_title="🦷 Zoe Dental", layout="wide")


st.markdown("""
<div style="display: flex; justify-content: center; align-items: center; flex-direction: column; margin-bottom: 40px;">
    <h1 style="color: #c1713b; font-size: 36px; margin-bottom: 10px;">Clinton Dental Services</h1>
    <h4 style="font-size: large; color: #c1713b; font-weight: bold; margin-top: 0;">Creating smiles, spreading joy</h4>
</div>
""", unsafe_allow_html=True)
  


# Carts Data 
cards_data = [
    {
        "image": "https://clintondentist.net/wp-content/uploads/2024/02/dental-fillings-parks-family-dentistry.jpg",
        "heading": "Stay One Step Ahead",
        "paragraph": "Revitalize your teeth with our thorough checkups and cleanings, leaving your pearly whites shining like a diamond.",
        "button_text": "See Cleanings"
    },
    {
        "image": "https://clintondentist.net/wp-content/uploads/2024/02/dental-bridge-parks-family-dentistry.jpg",
        "heading": "Traditional Crowns",
        "paragraph": "Meticulously crafted to restore your teeth’s strength and beauty — goodbye damaged teeth, hello healthy smile!",
        "button_text": "See Crowns"
    },
    {
        "image": "https://clintondentist.net/wp-content/uploads/2024/02/patient-consultation-dr-parks-clinton-parks-family-dental.jpg",
        "heading": "Dental Bridges",
        "paragraph": "Our dental bridges seamlessly fill spaces left by missing teeth, giving you a complete and confident smile.",
        "button_text": "See Bridges"
    },
    {
        "image": "https://clintondentist.net/wp-content/uploads/2024/02/parks-dental-56.jpg",
        "heading": "Same-Day Crowns",
        "paragraph": "Witness the transformation as we restore your smile to its former glory with CEREC same-day crowns that blend artistry and efficiency.",
        "button_text": "See CEREC Crowns"
    },
    {
        "image": "https://clintondentist.net/wp-content/uploads/2024/02/840-x-600.jpg",
        "heading": "Implant Restorations",
        "paragraph": "Our expert team will restore your implant with precision, providing a natural-looking tooth that renews your confidence.",
        "button_text": "See Restorations"
    },
    {
        "image": "https://clintondentist.net/wp-content/uploads/2024/02/dental-cleaning-parks-family-dentistry.jpg",
        "heading": "Nitrous Oxide",
        "paragraph": "Forget about dental anxiety — enjoy a relaxed dental experience while we work our magic with nitrous oxide sedation.",
        "button_text": "See Sedation"
    }
]



## Har row mein 3 cards display karne ke liye
for i in range(0, len(cards_data), 3):
    # Ek row (3 columns)
    cols = st.columns(3)
    
    # Har column mein ek card 
    for j in range(3):
        if i + j < len(cards_data):  
            card = cards_data[i + j]
            with cols[j]:
                # Card ka design
                st.markdown(f"""
                <div style="padding: 20px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 2px 2px 10px #aaa; margin-bottom: 20px;">
                    <img src="{card['image']}" alt="Clinic Image" style="width: 100%; border-radius: 5px;">
                    <h3>{card['heading']}</h3>
                    <p>{card['paragraph']}</p>
                     <button onclick="handleClick({i + j})" style="padding: 10px 20px; background-color: #c1713b; color: white; border: none; border-radius: 5px; cursor: pointer;">
                        {card['button_text']}
                </div>
                """, unsafe_allow_html=True)

