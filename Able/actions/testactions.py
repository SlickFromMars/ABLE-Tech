import actions.os_ops
import actions.greet
import actions.online_ops

if __name__ == '__main__':
    actions.online_ops.find_my_ip()
    print(*actions.online_ops.get_weather_report("Las Vegas"))

