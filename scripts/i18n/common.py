BOOK = "BOOK"

def callout(title: str, text: str, cta: str) -> str:
    return (
        f'<div class="svs-callout"><strong>{title}</strong> '
        f"{text} "
        f'<a class="svs-cta" href="{BOOK}">{cta}</a>'
        f"</div>"
    )
