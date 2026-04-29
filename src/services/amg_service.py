import subprocess
from src.core.logger_init import logger


def add_vpn_user(device_name: str) -> str:
    result = subprocess.run(
        ["bash", "/host_root/add_vpn_user.sh", device_name],
        capture_output=True,
        text=True,
    )

    conf_path = result.stdout.strip()

    if not conf_path or result.returncode != 0:
        logger.error(
            f"Не удалось выполнить команду для генерации конфига для {device_name}"
        )
        return

    qr_path = f"/tmp/{device_name}_qr.png"
    is_created_qr = subprocess.run(["qrencode", "-o", qr_path, "-r", conf_path])

    if not is_created_qr:
        logger.error(f"Не удалось создать qr код для {device_name}")

    return {"conf_path": conf_path, "qr_path": qr_path}
