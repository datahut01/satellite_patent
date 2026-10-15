# 모델명은 변경이 가능
# 단, 최신 gpt 모델의 경우, temperature 설정이 불필요함.
# 원격탐사를 위한 프롬프트
def check_satellite_remote_sensing_relevance2(
    patent_id: str,
    abstract: str,
    model: str = "gpt-4o-mini",
    seed: int = SEED
) -> dict:

    system_msg = (
    "You are an expert patent analyst specializing in remote sensing-related technologies and services. "
    "Determine whether the given patent abstract is relevant to the remote sensing-related industry. "
    "Remote sensing-related industry includes not only satellite-based Earth observation itself, "
    "but also value-added uses of remote sensing data, such as distribution and sales of satellite imagery or sensing products, "
    "information and communication services based on remote sensing data, data transmission and delivery services, "
    "platform operation, image-processing software, GIS applications, remote-sensing data analysis tools, "
    "and professional, scientific, and technical services such as interpretation, consulting, monitoring, and research support. "
    "Do not classify general satellite communication, launch systems, or non-remote-sensing technologies as relevant "
    "unless the abstract clearly involves remote sensing data, satellite imagery, or related remote sensing services. "
    "If relevant, output YES. If not relevant, output NO. "
    "Output only one word: YES or NO.")

    user_msg = f'''
    Patent Abstract:
    {abstract}
    
    Answer:
    '''.strip()
    start = time.perf_counter()

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg}
        ],
        temperature=0,
        seed=seed,
        max_completion_tokens=5
    )

    elapsed = time.perf_counter() - start

    raw_answer = (response.choices[0].message.content or "").strip().upper()
    answer = "YES" if raw_answer.startswith("YES") else "NO"

    return {
        "patent_id": patent_id,
        "answer": answer,
        "raw_output": raw_answer,
        "prompt_tokens": response.usage.prompt_tokens,
        "completion_tokens": response.usage.completion_tokens,
        "total_tokens": response.usage.total_tokens,
        "elapsed_sec": round(elapsed, 3),
        "model": response.model,
        "seed": seed,
        #"system_fingerprint": getattr(response, "system_fingerprint", None),
    }

# 위성방송통신을 위한 프롬프트
def check_satellite_remote_sensing_relevance2(
    patent_id: str,
    abstract: str,
    model: str = "gpt-4o-mini",
    seed: int = SEED
) -> dict:

    system_msg = (
    "You are an expert patent analyst specializing in satellite broadcasting and communications-related technologies and services. "
    "Determine whether the given patent abstract is relevant to the satellite broadcasting and communications industry. "
    "Satellite broadcasting and communications industry refers to the broad field of services and equipment manufacturing using broadcasting and communication satellites. "
    "It includes manufacturing of devices and terminal equipment used for satellite communication and broadcasting services, "
    "such as satellite signal receiving antennas, satellite phone terminals, satellite TV receivers, satellite communication modems, "
    "and other satellite broadcasting and communications equipment. "
    "It also includes distribution and sales of satellite broadcasting and communications equipment and components, "
    "such as sales of satellite TV receiving antennas, distribution of satellite communication parts, and retail of satellite terminals and related products. "
    "In addition, it includes satellite-based broadcasting and communication services and the software needed for them, "
    "such as operation of satellite communication networks, signal processing, broadcast scheduling management, development of related software, "
    "and provision of satellite-based broadcasting and communication services. "
    "It further includes professional, scientific, and technical services related to the construction and operation of satellite broadcasting and communications systems, "
    "such as satellite network design consulting, ground station installation and testing services, and consulting on satellite frequency allocation and coordination. "
    "It also includes construction of ground-based facilities and related structures for satellite broadcasting and communications, "
    "such as satellite communication antenna base stations, satellite broadcasting centers, control facilities, and satellite earth station installation works. "
    "Do not classify remote sensing, launch systems, satellite manufacturing in general, or non-satellite broadcasting or telecommunications technologies as relevant "
    "unless the abstract clearly involves satellite broadcasting and communications services, equipment, software, distribution, technical services, or infrastructure. "
    "If relevant, output YES. If not relevant, output NO. "
    "Output only one word: YES or NO."
)

    user_msg = f'''
    Patent Abstract:
    {abstract}
    
    Answer:
    '''.strip()
    start = time.perf_counter()

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg}
        ],
        temperature=0,
        seed=seed,
        max_completion_tokens=5
    )

    elapsed = time.perf_counter() - start

    raw_answer = (response.choices[0].message.content or "").strip().upper()
    answer = "YES" if raw_answer.startswith("YES") else "NO"

    return {
        "patent_id": patent_id,
        "answer": answer,
        "raw_output": raw_answer,
        "prompt_tokens": response.usage.prompt_tokens,
        "completion_tokens": response.usage.completion_tokens,
        "total_tokens": response.usage.total_tokens,
        "elapsed_sec": round(elapsed, 3),
        "model": response.model,
        "seed": seed,
        #"system_fingerprint": getattr(response, "system_fingerprint", None),
    }

# 위성항법을 위한 프롬프트
def check_satellite_remote_sensing_relevance2(
    patent_id: str,
    abstract: str,
    model: str = "gpt-4o-mini",
    seed: int = SEED
) -> dict:

    system_msg = (
    "You are an expert patent analyst specializing in satellite navigation-related technologies and services. "
    "Determine whether the given patent abstract is relevant to the satellite navigation industry. "
    "Satellite navigation industry refers to all fields related to navigation services and equipment manufacturing "
    "that use radio signals transmitted from satellites, either directly observed or relayed through reference or ground stations, "
    "to determine a user's location or guide a route. "
    "It includes manufacturing of devices and equipment related to satellite navigation, "
    "such as GNSS receiver chips, GPS receivers, antennas, in-vehicle and marine navigation devices, wearable GPS devices, "
    "and other products used to receive or utilize satellite navigation signals. "
    "It also includes distribution and sales of satellite navigation devices and related products, "
    "such as sales of GPS receivers and antennas, and distribution of positioning equipment, parts, and related navigation products. "
    "In addition, it includes communication services, location-information services, and software development using satellite navigation, "
    "such as real-time traffic navigation services, satellite augmentation signal services, location-tracking communication services for logistics and transport, "
    "location-based service (LBS) applications, vehicle navigation software, and GNSS signal-processing algorithms. "
    "Do not classify general satellite communication, remote sensing, launch systems, or non-navigation technologies as relevant "
    "unless the abstract clearly involves satellite navigation, GNSS, GPS, positioning, route guidance, "
    "or related satellite navigation devices, software, or services. "
    "If relevant, output YES. If not relevant, output NO. "
    "Output only one word: YES or NO."
)

    user_msg = f'''
    Patent Abstract:
    {abstract}
    
    Answer:
    '''.strip()
    start = time.perf_counter()

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg}
        ],
        temperature=0,
        seed=seed,
        max_completion_tokens=5
    )

    elapsed = time.perf_counter() - start

    raw_answer = (response.choices[0].message.content or "").strip().upper()
    answer = "YES" if raw_answer.startswith("YES") else "NO"

    return {
        "patent_id": patent_id,
        "answer": answer,
        "raw_output": raw_answer,
        "prompt_tokens": response.usage.prompt_tokens,
        "completion_tokens": response.usage.completion_tokens,
        "total_tokens": response.usage.total_tokens,
        "elapsed_sec": round(elapsed, 3),
        "model": response.model,
        "seed": seed,
        #"system_fingerprint": getattr(response, "system_fingerprint", None),
    }
