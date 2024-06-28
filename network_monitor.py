import psutil
import json
from flask import Flask, jsonify, render_template

app = Flask(__name__)

def get_network_stats():
    stats = psutil.net_io_counters(pernic=True)
    data = {}
    for nic, addrs in stats.items():
        data[nic] = {
            'bytes_sent': addrs.bytes_sent,
            'bytes_recv': addrs.bytes_recv,
            'packets_sent': addrs.packets_sent,
            'packets_recv': addrs.packets_recv,
            'errin': addrs.errin,
            'errout': addrs.errout,
            'dropin': addrs.dropin,
            'dropout': addrs.dropout,
        }
    return data

@app.route('/api/network_stats', methods=['GET'])
def network_stats():
    stats = get_network_stats()
    return jsonify(stats)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
