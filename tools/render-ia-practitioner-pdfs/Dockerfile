FROM debian:bookworm-slim

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    ca-certificates \
    fonts-dejavu \
    lmodern \
    pandoc \
    texlive-fonts-recommended \
    texlive-latex-recommended \
    texlive-xetex \
  && rm -rf /var/lib/apt/lists/*

COPY render.sh /usr/local/bin/render-ia-practitioner-pdfs
RUN chmod +x /usr/local/bin/render-ia-practitioner-pdfs

ENTRYPOINT ["/usr/local/bin/render-ia-practitioner-pdfs"]
